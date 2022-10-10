"""adding label and content label and modifiyng content model

Revision ID: 3fb19c5ff74f
Revises: 605940aed2e3
Create Date: 2022-09-14 14:30:49.290380

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3fb19c5ff74f'
down_revision = '605940aed2e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('labels',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('label_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content_labels',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('content_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('label_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['content_id'], ['contents.id'], ),
    sa.ForeignKeyConstraint(['label_id'], ['labels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('contents', sa.Column('slug', sa.String(length=300), nullable=True))
    op.add_column('contents', sa.Column('is_published', sa.Boolean(), nullable=True))
    op.add_column('contents', sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('contents', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.create_unique_constraint(None, 'contents', ['slug'])
    op.create_foreign_key(None, 'contents', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contents', type_='foreignkey')
    op.drop_constraint(None, 'contents', type_='unique')
    op.drop_column('contents', 'updated_at')
    op.drop_column('contents', 'user_id')
    op.drop_column('contents', 'is_published')
    op.drop_column('contents', 'slug')
    op.drop_table('content_labels')
    op.drop_table('labels')
    # ### end Alembic commands ###