"""Initial migration

Revision ID: 430559e6bb3a
Revises: 
Create Date: 2022-08-20 18:28:14.254145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '430559e6bb3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plans',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('days_add', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('persian_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('triggers',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('persian_name', sa.String(length=255), nullable=True),
    sa.Column('platform', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=13), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('role_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('chatflows',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connections',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('application_name', sa.String(length=255), nullable=True),
    sa.Column('account_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_id', 'application_name')
    )
    op.create_table('credits',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('to_datetime', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facebook_accounts',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('facebook_user_long_lived_token', sa.String(length=255), nullable=True),
    sa.Column('facebook_user_id', sa.String(length=255), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('price', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connection_chatflows',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('connection_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('trigger_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('chatflow_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['chatflow_id'], ['chatflows.id'], ),
    sa.ForeignKeyConstraint(['connection_id'], ['connections.id'], ),
    sa.ForeignKeyConstraint(['trigger_id'], ['triggers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instagram_pages',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('facebook_account_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('facebook_page_id', sa.String(length=255), nullable=True),
    sa.Column('instagram_page_id', sa.String(length=255), nullable=True),
    sa.Column('facebook_page_token', sa.String(length=255), nullable=True),
    sa.Column('instagram_username', sa.String(length=255), nullable=True),
    sa.Column('instagram_profile_picture_url', sa.String(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['facebook_account_id'], ['facebook_accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nodes',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('chatflow_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('from_widget', postgresql.ARRAY(postgresql.UUID()), nullable=True),
    sa.Column('widget', sa.JSON(), nullable=True),
    sa.Column('is_head', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['chatflow_id'], ['chatflows.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nodes')
    op.drop_table('instagram_pages')
    op.drop_table('connection_chatflows')
    op.drop_table('transactions')
    op.drop_table('facebook_accounts')
    op.drop_table('credits')
    op.drop_table('connections')
    op.drop_table('chatflows')
    op.drop_table('users')
    op.drop_table('triggers')
    op.drop_table('roles')
    op.drop_table('plans')
    # ### end Alembic commands ###
